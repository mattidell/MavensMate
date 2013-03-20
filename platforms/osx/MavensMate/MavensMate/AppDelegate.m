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
    [loadingWindow setLevel:kCGMainMenuWindowLevel-1];
    [loadingWindow setCollectionBehavior:NSWindowCollectionBehaviorStationary|NSWindowCollectionBehaviorCanJoinAllSpaces|NSWindowCollectionBehaviorFullScreenAuxiliary];
    
    [pluginsWindow setLevel:kCGMainMenuWindowLevel-1];
    [pluginsWindow setCollectionBehavior:NSWindowCollectionBehaviorStationary|NSWindowCollectionBehaviorCanJoinAllSpaces|NSWindowCollectionBehaviorFullScreenAuxiliary];
    
    [successWindow setLevel:kCGMainMenuWindowLevel-1];
    [successWindow setCollectionBehavior:NSWindowCollectionBehaviorStationary|NSWindowCollectionBehaviorCanJoinAllSpaces|NSWindowCollectionBehaviorFullScreenAuxiliary];
    
    
    statusItem = [[NSStatusBar systemStatusBar] statusItemWithLength:NSVariableStatusItemLength];
    [statusItem setMenu:statusMenu];
    [statusItem setImage:[NSImage imageNamed:@"MavensMateMenuBarIconNew"]];
    [statusItem setAlternateImage:[NSImage imageNamed:@"MavensMateMenuBarIconHighlightedWhite"]];
    [statusItem setHighlightMode:YES];
    [pluginsToolbar setSelectedItemIdentifier:@"stPluginTab"];
    
    
    [stButton setTitle:@"Install"];
    
    [self startServer];
}

- (NSArray *)toolbarSelectableItemIdentifiers: (NSToolbar *)toolbar;
{
    // Optional delegate method: Returns the identifiers of the subset of
    // toolbar items that are selectable. In our case, all of them
    return [NSArray arrayWithObjects:stToolbarItem, nil];
}

-(IBAction) showSublimeTextPluginPanel: (id) sender {
    //[pluginsToolbar set
}

//opens plugins window when menu item is clicked
-(void) openSuccessWindow {
    //if(! [pluginsWindow isVisible] )
    [NSApp activateIgnoringOtherApps:YES];
    [successWindow makeKeyAndOrderFront:nil];
}

-(IBAction) closeSuccessWindow:(id)sender {
    [successWindow close];
}

//opens plugins window when menu item is clicked
-(IBAction) openPluginsWindow:(id)sender {
    //if(! [pluginsWindow isVisible] )
    [NSApp activateIgnoringOtherApps:YES];
    [pluginsWindow makeKeyAndOrderFront:sender];
}

-(void) downloadAndInstallSublimeTextPlugin {
    NSError *error;
    
    NSString* stPackagesPath;
    stPackagesPath = [@"~/Library/Application Support/Sublime Text 2/Packages/MavensMate-SublimeText-2.0" stringByExpandingTildeInPath];
    
    NSFileManager *filemgr;
    filemgr = [NSFileManager defaultManager];

    NSString *filePath = [NSTemporaryDirectory() stringByAppendingPathComponent:@"mavensmate.zip"];
    //clean up tmp directory
    if ([filemgr removeItemAtPath:filePath error:&error] != YES)
        NSLog(@"Unable to remove zip from tmp path: %@", [error localizedDescription]);
    
    //download latest version
    NSString *myurl = @"https://github.com/joeferraro/MavensMate-SublimeText/archive/2.0.zip";
    NSData* data = [NSData dataWithContentsOfURL:[NSURL URLWithString:myurl]];
    [data writeToFile:filePath atomically:YES];
    
    //change directory to tmp (where file is downloaded)
    if ([filemgr changeCurrentDirectoryPath: NSTemporaryDirectory()] == NO)
        NSLog (@"Cannot change directory.");
    
    //unzip the file
    NSString *path = @"/usr/bin/unzip";
    NSArray *args = [NSArray arrayWithObjects:@"mavensmate.zip", nil];
    [[NSTask launchedTaskWithLaunchPath:path arguments:args] waitUntilExit];
    
    //clean up existing installation
    if ([filemgr removeItemAtPath:stPackagesPath error:&error] != YES)
        NSLog(@"Unable to remove MavensMate from packages path: %@", [error localizedDescription]);

    //move fresh installation to packages path
    NSString *origin = [NSTemporaryDirectory() stringByAppendingString:@"MavensMate-SublimeText-2.0"];
    //NSLog(origin);
    //NSLog(stPackagesPath);
    
    if ([filemgr moveItemAtPath:origin toPath:stPackagesPath error:&error] != YES)
        NSLog(@"Unable to move file: %@", [error localizedDescription]);
    
    //clean up tmp directory
    if ([filemgr removeItemAtPath:filePath error:&error] != YES)
        NSLog(@"Unable to remove downloaded zip from tmp path: %@", [error localizedDescription]);
    
    [self performSelectorOnMainThread:@selector(hideLoading) withObject:nil waitUntilDone:NO];
    [self openSuccessWindow];

}

-(void) showLoading {
    [loadingbar startAnimation:self];
    [NSApp activateIgnoringOtherApps:YES];
    [loadingWindow makeKeyAndOrderFront:nil];
}

-(void) hideLoading {
    [loadingbar stopAnimation:self];
    [loadingWindow close];
}

//directs user to sublime text github page to download
-(IBAction) goToSublimeTextPluginPage:(id)sender {
    //NSURL *url = [NSURL URLWithString:@"https://github.com/joeferraro/MavensMate-SublimeText"];
    //if( ![[NSWorkspace sharedWorkspace] openURL:url] )
        //NSLog(@"Failed to open url: %@",[url description]);
    [self showLoading];
    [self performSelectorInBackground:@selector(downloadAndInstallSublimeTextPlugin) withObject:nil];
}



//local server related actions

-(IBAction) restartServer:(id)sender {
    [self stopServer];
    [self startServer];
}

-(void) stopServer {
    system("killAll mmserver");
}

-(void)applicationWillTerminate:(NSNotification *)notification {
    [self stopServer];
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