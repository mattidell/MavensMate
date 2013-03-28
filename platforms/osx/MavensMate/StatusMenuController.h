//
//  StatusMenuController.h
//  MavensMate
//
//  Created by Joseph on 3/22/13.
//  Copyright (c) 2013 Joseph. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "DragAndDropStatusMenuView.h"

@class PluginsController;
@class AboutController;

@interface StatusMenuController : NSViewController {
@private
    IBOutlet NSMenu *_statusMenu;
    NSStatusItem *_statusItem;
}

@property (strong) PluginsController *pluginsController;
@property (strong) AboutController *aboutController;

-(StatusMenuController*)init;
-(IBAction)openPluginsView:(id)sender;
-(IBAction)openAboutView:(id)sender;
-(IBAction)restartServer:(id)sender;
-(void)showMenu;


@end
