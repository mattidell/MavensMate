import urlparse

def project_request(requestHandler):
    # params = get_request_params(requestHandler)

    # request_id, tmp_directory = MavensMate::FileFactory.get_request_id_and_put_tmp_directory
    # Thread.new {
    #     body = ""
    #     begin
    #         params = {}
    #         params[:action]     = req["action"]
    #         params[:pn]         = req["pn"]
    #         params[:un]         = req["un"]
    #         params[:pw]         = req["pw"]
    #         params[:server_url] = req["server_url"]
    #         params[:vc_un]      = req["vc_un"]
    #         params[:vc_pw]      = req["vc_pw"]
    #         params[:vc_url]     = req["vc_url"]
    #         params[:vc_type]    = req["vc_type"]
    #         params[:vc_alias]   = req["vc_alias"]
    #         params[:vc_branch]  = req["vc_branch"]
    #         params[:package]    = eval(req["tree"]) if params[:action] == "new"
    #         params[:where]      = req["where"] 
    #         ENV["MM_WORKSPACE"] = req["where"]

    #         if params[:action] == "checkout"
    #           result = MavensMate.checkout_project(params)
    #         else
    #           result = MavensMate.new_project(params)
    #         end
    #         if result[:success]
    #           body = result.to_json
    #           res = {
    #             :success    => true, 
    #             :body       => "project created successfully",
    #             :body_type  => "text"
    #           }
    #           body = res.to_json
    #           project_file = File.join(ENV['MM_WORKSPACE'], params[:pn], params[:pn]+".sublime-project")
    #           `killAll MavensMate` 
    #           `'/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl' --project '#{project_file}'`
    #         else
    #           body = result.to_json
    #         end
    #     rescue Exception => e
    #         res = {
    #           :success    => false, 
    #           :body       => e.message + "\n\n" + e.backtrace.join("\n"),
    #           :body_type  => "text"
    #         }
    #         body = res.to_json
    #     end
    #     File.open("#{tmp_directory}/.response", 'w') {|f| f.write(body) }
    # }
    # MavensMate::LocalServerThin.respond_with_async_request_id(request_id)

    # respond(requestHandler, 'text/html', 'foobahhhh')
    pass

def auth_request(requestHandler):
    params = get_request_params(requestHandler)
    respond(requestHandler, 'text/html', 'foobahhhh')

def metadata_list_request(requestHandler):
    requestHandler.send_response(200)
    requestHandler.send_header('Content-type', 'text/html')
    requestHandler.end_headers()
    requestHandler.wfile.write("dfjklsjsfkdlsfjdklsfdjklsdfjklsfdjklfdjklfdjklsfdjkldfkljdflkj")
    requestHandler.wfile.close()

def version_control_request(requestHandler):
    requestHandler.send_response(200)
    requestHandler.send_header('Content-type', 'text/html')
    requestHandler.end_headers()
    requestHandler.wfile.write("dfjklsjsfkdlsfjdklsfdjklsdfjklsfdjklfdjklfdjklsfdjkldfkljdflkj")
    requestHandler.wfile.close()

mappings = {
    '/project'           : { 'GET' : project_request }, 
    '/project/edit'      : { 'GET' : project_request }, 
    '/project/existing'  : { 'GET' : project_request }, 
    '/metadata/list'     : { 'GET' : metadata_list_request }, 
    '/vc'                : { 'GET' : version_control_request },
    '/auth'              : { 'GET' : auth_request }
    # '/test'              : { 'GET' : unit_test_request }, 
    # '/metadata/index'    : { 'GET' : metadata_index_request }, 
    # '/deploy'            : { 'GET' : deploy_request }, 
    # '/execute'           : { 'GET' : execute_apex_request }, 
    # '/connections'       : { 'GET' : deployment_connections_request }, 
    # '/status'            : { 'GET' : status_request }     
}

def get_request_params(requestHandler):
    params = {}
    path = requestHandler.path
    if '?' in path:
        path, tmp = path.split('?', 1)
        params = urlparse.parse_qs(tmp)
    return params

def respond(requestHandler, type, body):
    requestHandler.send_response(200)
    requestHandler.send_header('Content-type', type)
    requestHandler.send_header('Access-Control-Allow-Origin', '*')
    requestHandler.end_headers()
    requestHandler.wfile.write(body)
    requestHandler.wfile.close()