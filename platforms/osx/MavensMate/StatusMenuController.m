//
//  StatusMenuController.m
//  MavensMate
//
//  Created by Joseph on 3/22/13.
//  Copyright (c) 2013 Joseph. All rights reserved.
//

#import "StatusMenuController.h"
#import "DragAndDropStatusMenuView.h"
#import "PluginsController.h"

@implementation StatusMenuController

@synthesize pluginsController = _pluginsController;
 
//@synthesize _statusItem = statusItem;

-(StatusMenuController*)init {
    self = [super init];
	if (self) { 
		//Initialization code goes here
	}
	return self; 
}

-(void) awakeFromNib {
    NSStatusBar *statusBar = [NSStatusBar systemStatusBar];
	_statusItem = [statusBar statusItemWithLength:NSVariableStatusItemLength];
    [_statusItem setAlternateImage:[NSImage imageNamed:@"MavensMateMenuBarIconHighlightedWhite"]];
    [_statusItem setHighlightMode:YES];
    
	DragAndDropStatusMenuView *dragAndDropView = [[DragAndDropStatusMenuView alloc]
												  initWithFrame:NSMakeRect(0, 0, 22, 22)];
	dragAndDropView.statusItem = _statusItem;
	[dragAndDropView setMenu:_statusMenu];
	[_statusItem setView:dragAndDropView];
}

-(void)showMenu {
    [_statusItem popUpStatusItemMenu:_statusMenu];
}

-(IBAction)openPluginsView:(id)sender {
    //if(!_pluginsController) {
        _pluginsController = [[PluginsController alloc] init];
	//}
    [[_pluginsController window] makeKeyAndOrderFront:nil];
    [[NSApplication sharedApplication] arrangeInFront:nil];
}

//local server related actions
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
