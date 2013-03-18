import os
import random
import string
import tempfile
import json
import shutil
import threading
import subprocess
import pipes
import lib.config as global_config
#from jinja2 import Environment, FileSystemLoader
tmp_dir = tempfile.gettempdir()

#this function is only used on async requests
def get_request_id_and_put_tmp_directory():
    request_id = get_random_string()
    tmp_directory_location = put_tmp_directory_on_disk(request_id)
    return request_id, tmp_directory_location

#this function is only used on async requests
def generate_request_id():
    return get_random_string()

#this function is only used on async requests
def put_tmp_directory_on_disk(request_id=None):
    if request_id == None:
        request_id = get_random_string()
    mm_tmp_directory = "{0}/.org.mavens.mavensmate.{1}".format(tmp_dir, request_id)
    os.makedirs(mm_tmp_directory)
    return mm_tmp_directory

#retrieves the response from the tmp directory
def get_request_response(request_id, convert_to_string=True, remove_request_directory=True):
    location = "{0}/.org.mavens.mavensmate.{1}".format(tmp_dir, request_id)
    try:
        # response_body = open(location+"/.response")
        # response = json.load(response_body)
        # response_body.close()
        #if convert_to_string == True:
        #    response = json.dumps(response) 
        response_file = open(location+"/.response", "r")
        response = response_file.read()
        response_file.close()
    except:
        response = "error reading response file"
    #if remove_request_directory == True:
    #    shutil.rmtree(location)
    return response

def get_random_string(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

#if the worker has placed the .response file in the tmp directory, we're ready to respond
def get_request_status(request_id):
    if os.path.exists("{0}/.org.mavens.mavensmate.{1}".format(tmp_dir, request_id)):
        if os.path.isfile("{0}/.org.mavens.mavensmate.{1}/.response".format(tmp_dir, request_id)):
            response = {
                "status" : "complete",
                "ready"  : True
            }
            return response
        else:
            response = {
                "status" : "pending",
                "ready"  : False  
            }
            return response
    else:
        response = {
            "status" : "error",
            "body"   : "path does not exist"
        }
        return response

#the main job of the backgroundworker is to submit a request for work to be done by mm
class BackgroundWorker(object):
    def __init__(self, operation, params, async, request_id=None, payload=None, queue=None):
        self.operation  = operation
        self.params     = params
        self.request_id = request_id
        self.async      = async
        self.payload    = payload
        self.response   = None
        self.queue      = queue

    def run(self):
        mm_response = None
        args = self.get_arguments()
        p = subprocess.Popen("{0} {1}".format(pipes.quote(global_config.mm_path), args), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        p.stdin.write(self.payload)
        p.stdin.close()
        if p.stdout is not None: 
            mm_response = p.stdout.readlines()
        elif p.stderr is not None:
            mm_response = p.stderr.readlines()
        response_body = '\n'.join(mm_response)
        self.response = response_body
        self.finish()
        if self.async == True:
            self.queue.put(response_body)
        else:
            return response_body

    def finish(self):
        if self.operation == 'new_project' or self.operation == 'checkout_project':
            print self.response
            if json.loads(self.response)['success'] == True:
                os.system('killAll MavensMateWindowServer')

    def get_arguments(self):
        args = {}
        args['-o'] = self.operation #new_project, get_active_session

        if self.operation == 'new_project':
            pass
        elif self.operation == 'checkout_project':
            pass  
        elif self.operation == 'get_active_session':
            pass 
        elif self.operation == 'update_credentials':
            pass
        elif self.operation == 'execute_apex':
            pass
        elif self.operation == 'deploy':
            args['--html'] = None
        elif self.operation == 'unit_test':
            args['--html'] = None
        elif self.operation == 'index_metadata':
            args['--html'] = None    
                
        arg_string = []
        for x in args.keys():
            if args[x] != None:
                arg_string.append(x + ' ' + args[x] + ' ')
            else:
                arg_string.append(x + ' ')
        stripped_string = ''.join(arg_string).strip()
        return stripped_string

