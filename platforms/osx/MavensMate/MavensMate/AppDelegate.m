//
//  AppDelegate.m
//
//  Created by Joseph Ferraro on 2/23/12.
//  Copyright (c) 2013 Joseph Ferraro. All rights reserved.
//

#import "AppDelegate.h"
#import "StatusMenuController.h"


@implementation AppDelegate

@synthesize menuController = _menuController;

- (void)applicationDidFinishLaunching:(NSNotification *)aNotification {
    //[self setupDefaults];
    _menuController = [[StatusMenuController alloc] init];
	[NSBundle loadNibNamed:@"StatusMenu" owner:_menuController];
}

- (void)setupDefaults {
    // future functionality
    //[[[NSUserDefaultsController sharedUserDefaultsController] values] setValue:[NSNumber numberWithBool:YES]
    //                                  forKey:@"stBeta"];
}


//**********************************
//** local server related actions **
//**********************************

-(void)applicationWillTerminate:(NSNotification *)notification {
    //[self stopServer];
}

@end