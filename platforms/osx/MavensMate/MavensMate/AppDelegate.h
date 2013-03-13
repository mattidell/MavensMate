//
//  AppDelegate.h
//  StatusBar
//
//  Created by Julian Meyer on 9/23/12.
//  Copyright (c) 2012 Julian Meyer. All rights reserved.
//

#import <Cocoa/Cocoa.h>

@interface AppDelegate : NSObject <NSApplicationDelegate> {
    IBOutlet NSMenu *statusMenu;
    IBOutlet NSMenuItem *serverItem;
    NSStatusItem * statusItem;
}

-(IBAction)toggleServer:(id)sender;

@end