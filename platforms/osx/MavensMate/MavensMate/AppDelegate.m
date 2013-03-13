//
//  PDAppDelegate.m
//  StatusBar
//
//  Created by Julian Meyer on 9/23/12.
//  Copyright (c) 2012 Julian Meyer. All rights reserved.
//

#import "AppDelegate.h"

@implementation AppDelegate

- (void)applicationDidFinishLaunching:(NSNotification *)aNotification
{
    statusItem = [[NSStatusBar systemStatusBar] statusItemWithLength:NSVariableStatusItemLength];
    [statusItem setMenu:statusMenu];
    [statusItem setImage:[NSImage imageNamed:@"MavensMateMenuBarIconNew"]];
    [statusItem setAlternateImage:[NSImage imageNamed:@"MavensMateMenuBarIconHighlightedWhite"]];
    [statusItem setHighlightMode:YES];
    
    [self startServer];
}

-(void)applicationWillTerminate:(NSNotification *)notification {
    [self stopServer];
}

-(IBAction) restartServer:(id)sender {
    [self stopServer];
    [self startServer];
}

-(void) stopServer {
    system("killAll mmserver");
}

-(void) startServer {
    [self performSelectorInBackground:@selector(startServerInBackground) withObject:nil];
}

-(void) startServerInBackground {
    NSBundle*mainBundle=[NSBundle mainBundle];
    NSTask *task;
    task = [[NSTask alloc] init];
    NSString*mmpath=[mainBundle pathForResource:@"mm" ofType:(nil) inDirectory:(@"mm")];
    NSString*mmserverpath=[mainBundle pathForResource:@"mmserver" ofType:(nil) inDirectory:(@"mmserver")];
    
    [task setLaunchPath: mmserverpath];
    
    NSArray *arguments;
    arguments = [NSArray arrayWithObjects: @"-m", mmpath, nil];
    [task setArguments: arguments];
    
    NSPipe *pipe;
    pipe = [NSPipe pipe];
    [task setStandardOutput: pipe];
    
    
    NSFileHandle *file;
    file = [pipe fileHandleForReading];
    
    [task launch];
    
    // need to rework this to be non-blocking
    //    NSData *data;
    //    data = [file readDataToEndOfFile];
    //
    //    NSString *string;
    //    string = [[NSString alloc] initWithData: data encoding: NSUTF8StringEncoding];
    //    NSLog (@"grep returned:\n%@", string);
    
    //[string release];
    //return string;
    //[task release];
}


@end