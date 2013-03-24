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

@interface StatusMenuController : NSViewController {
@private
    IBOutlet NSMenu *_statusMenu;
    NSStatusItem *_statusItem;
}

@property (strong) PluginsController *pluginsController;


-(StatusMenuController*)init;
-(IBAction)openPluginsView:(id)sender;
-(IBAction)restartServer:(id)sender;
-(void)showMenu;


@end
