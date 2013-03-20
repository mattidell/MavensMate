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
    IBOutlet NSMenuItem *pluginsItem;
    IBOutlet NSWindow *pluginsWindow;
    IBOutlet NSToolbar *pluginsToolbar;
    IBOutlet NSToolbarItem *stToolbarItem;
    IBOutlet NSView *stPluginView;
    NSStatusItem * statusItem;
    IBOutlet NSWindow *loadingWindow;
    IBOutlet NSProgressIndicator *loadingbar;
    IBOutlet NSWindow *successWindow;
    IBOutlet NSButton *successOKButton;
    IBOutlet NSButton *stButton;
}

- (NSArray *)toolbarSelectableItemIdentifiers:(NSToolbar *)toolbar;

-(IBAction)showSublimeTextPluginPanel: (id) sender;

-(IBAction)toggleServer:(id)sender;

@end