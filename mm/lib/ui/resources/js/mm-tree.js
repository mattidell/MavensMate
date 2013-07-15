var itemRightClickMenu = new Ext.menu.Menu({
    items: [{
        text: 'Refresh metadata from server',
        handler: function(item) {
            console.log(item)
            
            $.ajax({
                type: "POST",
                url: "http://127.0.0.1:9000/project/refresh_index", 
                data: JSON.stringify({
                    metadata_types   : [item.parentMenu.apexMetadataType],
                    project_name    : get_project_name()
                }),
                beforeSend: function() { showLoading("Refreshing Metadata Type: "+ item.parentMenu.apexMetadataType +"..."); },
                complete: function(data){
                    reloadTree()
                } 
            });
        }
    }]
});

Ext.define('Ext.ux.grid.mm-tree', {
    extend: 'Ext.tree.Panel',
    rootVisible: true,
    // mask: true,
    // maskConfig: { msg: "Loading tree items..." },
    // loadMask: true,
    useArrows: true,
    frame: false,
    header: false,
    style: 'margin: 0px 0px',
    disabledCls: 'x-tree-checkbox-checked-disabled',
    ALL_ID: 1,
    returnLeafsOnly: true,
    selectedIds: '',
    selModel: new Ext.selection.TreeModel({
        mode: 'MULTI',
        ignoreRightMouseSelection: true
    }),
    listeners: {
        load: function() {
            if (this.selectedIds === '') {
                this.selectedIds = []
                var ids = []
                var selected = this.getView().getChecked()
                Ext.Array.each(selected, function(item){
                   ids.push(item['internalId']) 
                })
                this.selectedIds = ids
            }
            //console.log('loading into tree!')
            //console.log(this.selectedIds)
            this.setSelections(this.selectedIds)
            hideLoading()
        },
        checkchange: function (node, check) {
            var me = this;

            node.set('cls', '');
            me.updateParentCheckedStatus(node);

            //if top-level is checked, select all below
            if (node.hasChildNodes()) {
                node.eachChild(this.setChildrenCheckedStatus);
            }

            //if this is the root id, check everything
            if (node.get('id') == this.ALL_ID) {
                //debug('[root checked]');
                //unsetThirdState for all
                me.getRootNode().cascadeBy(function () {
                    me.unsetThirdState(this);
                });
            }

            if (check) {
                //console.log('new node checked, adding to selected ids: ',node.get('id'))
                tree.selectedIds.push(node.get('id'));
                //console.log(tree.selectedIds)
            } else {
                //console.log('node unchecked, removing from selected ids: ')
                //console.log(tree.selectedIds)
                var index = tree.selectedIds.indexOf(node.get('id'));
                tree.selectedIds.splice(index, 1);
                //console.log(tree.selectedIds)
            }
        },
        beforeitemclick: function(dv, record, item, index, e) {
            // if (isTreeFiltered) {
            //     console.log('before click');
            //     e.preventDefault();
            //     return false;
            // }
        },
        beforeitemdblclick: function(dv, record, item, index, e) {
            // if (isTreeFiltered) {
            //     console.log('before click');
            //     e.preventDefault();
            //     return false;
            // }
        },
        itemcontextmenu: function(view, record, item, index, event) {
            console.log(record)
            console.log(item)
            if (record.data.depth == 1) {
                itemRightClickMenu.showAt(event.getXY());
                itemRightClickMenu.apexMetadataType = record.data.text;
                event.stopEvent();
            }
        }
    },

    // Propagate change downwards (for all children of current node).
    setChildrenCheckedStatus: function (current) {

        // if not root checked
        if (current.parentNode) {
            var parent = current.parentNode;
            current.set('checked', parent.get('checked'));
            if (current.get('checked')) {
                tree.selectedIds.push(current.get('id'));
            } else {
                var index = tree.selectedIds.indexOf(current.get('id'));
                tree.selectedIds.splice(index, 1);  
            }
        }

        if (current.hasChildNodes()) {
            //console.log('propping to children')
            //console.log(arguments.callee)
            current.eachChild(arguments.callee);
        }
    },

    // Propagate change upwards (if all siblings are the same, update parent).
    updateParentCheckedStatus: function (current) {
        //console.log('proppin upwards!')
        //console.log(current.get('text'))
        var me = this,
            currentChecked = current.get('checked'),
            currentId = current.get('id');

        current.eachChild(function (n) {
            //console.log('CHILD: ' +n.get('cls'))

            if (n.get('cls') == 'x-tree-checkbox-checked-disabled') {
                //console.log('CHILD IS THIRD STATE')
                current.set('cls', 'x-tree-checkbox-checked-disabled');
                current.set('checked', false);
                return true;
            }
        });

        //if this node has a parent
        if (current.parentNode) {

            var parent = current.parentNode;
            var checkedCount = 0;
            var checkedCountChildren = 0;
            parent.eachChild(function (n) {
                // debug( n.get('text'))
                checkedCount += (n.get('checked') ? 1 : 0);
            });

            current.eachChild(function (n) {
                // debug( n.get('text'))
                checkedCountChildren += (n.get('checked') ? 1 : 0);
            });

            // Children have same value if all of them are checked or none is checked.
            var allMySiblingsHaveSameValue = (checkedCount == parent.childNodes.length) || (checkedCount == 0);
            var allMyChildrenHaveSameValue = (checkedCountChildren == current.childNodes.length) || (checkedCountChildren == 0);

            var setParentVoid = true;

            // check if current node has any visible state.
            if (me.isThirdState(current) || currentChecked) {
                setParentVoid = false;
            }

            // if not - clear parent`s class
            if (setParentVoid) {
                me.unsetThirdState(parent);
            }

            if (allMySiblingsHaveSameValue) {

                // All  the Siblings  are same, so apply value to the parent.
                var checkedValue = (checkedCount == parent.childNodes.length);
                parent.set('checked', checkedValue);

                me.unsetThirdState(parent);
                // modify  Root based on it`s Children Have Same Value

                if (parent == me.getRootNode()) {
                    if (allMyChildrenHaveSameValue) {
                        me.unsetThirdState(me.getRootNode());
                    } else {
                        me.setThirdState(me.getRootNode());
                    }
                }


            } else {

                // Not all  the children are same, so set root node to third state.

                me.setThirdState(me.getRootNode());

                if (checkedCount) {
                    // At least one sibling is checked, so set parent node to third state.
                    me.setThirdState(parent);
                } else {

                    parent.set('checked', false);
                }


            }

            me.updateParentCheckedStatus(parent);
        }
    },

    isThirdState: function (node) {
        return  node.get('cls') == this.disabledCls;

    },

    setThirdState: function (node) {
        node.set('cls', this.disabledCls);
        node.set('checked', false);
    },

    unsetThirdState: function (node) {
        node.set('cls', '');
    },

    getPackage: function() {
        var json = { }
        var child_def = {}
        for (item in child_metadata) {
            child_def[child_metadata[item]['tagName']] = child_metadata[item]['xmlName']
        }
        try {
            var records = this.getView().getChecked(), names = [];
            Ext.Array.each(records, function(rec){
                if (rec.data.depth == 1) {
                    if (json[rec.parentNode.data.text] === undefined) {
                        try {
                            if (Object.prototype.toString.call(rec.raw.type.childXmlNames) === '[object Array]') {
                                if (rec.raw.type.childXmlNames.length == 0) {
                                    json[rec.data.text] = '*'
                                } else {
                                    json[rec.data.text] = []
                                }
                            } else {
                                json[rec.data.text] = '*'
                            }
                        } catch(e) {
                            json[rec.data.text] = '*'
                        }
                        
                    }
                } else if (rec.data.depth == 2) {
                    if (json[rec.parentNode.data.text] === undefined) {
                        json[rec.parentNode.data.text] = []
                        json[rec.parentNode.data.text].push(rec.data.text)
                    } else if (json[rec.parentNode.data.text] !== '*') {
                        json[rec.parentNode.data.text].push(rec.data.text)
                    }
                } else if (rec.data.depth == 3) {
                    if (rec.parentNode.parentNode.raw.type.inFolder) {
                        if (json[rec.parentNode.parentNode.data.text] === undefined) {
                            json[rec.parentNode.parentNode.data.text] = []
                        }
                        //this is a folder name, add it
                        json[rec.parentNode.parentNode.data.text].push(rec.parentNode.data.text + "/" + rec.data.text)
                    } else {
                        //this is a sub type like a custom field, list view, etc.
                        metadata_type = child_def[rec.data.text]
                        if (!json[metadata_type]) {
                            json[metadata_type] = []
                        } 

                        Ext.Array.each(rec.childNodes, function(childNode){
                            if (childNode.data.checked) {
                                json[metadata_type].push(childNode.parentNode.parentNode.data.text+"."+childNode.data.text)  
                            }
                        })
                    } 
                } else if (rec.data.depth == 4) {
                    //this is a child metadata object, like a custom field
                    metadata_type = child_def[rec.parentNode.data.text]
                    if (!json[metadata_type]) {
                        json[metadata_type] = []
                    } 
                    json[metadata_type].push(rec.parentNode.parentNode.data.text+"."+rec.data.text) 
                }
            })  
        } catch(e) {
            console.log(e)
            return []
        }
        return json
    },

    getSelections: function (id_only) {
        var me = this;

        //debug('[accessPanel getSelections]');

        try {
            var grid_selections = me.getView().getChecked(),
                allFound = false,
                result = [];


            Ext.Array.each(grid_selections, function (rec) {

                var pushdata = false;

                //  find all checked items
                if (rec.get('id') ) {

                    if (me.returnLeafsOnly ){
                        if (rec.get('leaf') === true){
                            pushdata = true;
                        }
                    }   else{
                        pushdata = true;
                    }
                    if (pushdata){
                        result.push(id_only == true ?  rec.get('id') : {id: rec.get('id')});
                    }

                }

                //  if NODE 'ALL' checked  - no children required
                if (rec.get('id') == me.ALL_ID) {
                    allFound = true;
                }
            });


            if (allFound) {
                result = id_only ? [  me.ALL_ID ] : [ {id: me.ALL_ID} ];
            }

            //debug(result);
            return result;
        } catch (e) {

            debug('[error in accessPanel getSelections]');
            debug(e);
        }
    },

    setSelections: function (ids) {

        var me = this;
        //  me.stopListener = true;

        //debug('[accessPanel setSelections]');
        // debug(ids);


        if (ids[0] && ids[0]['id']){

            ids = Ext.Array.pluck(ids, 'id');
        }

        // check RootNode or do cascade checking

        if (ids.indexOf(me.ALL_ID) > -1) {
            me.getRootNode().set('checked', true);
            me.getRootNode().eachChild(me.setChildrenCheckedStatus);
        } else {


            me.getRootNode().cascadeBy(function () {

                var currNode = this;

                if (currNode.get('leaf')) {
                    currNode.set('checked', ids.indexOf(currNode.get('id')) > -1);
                    me.updateParentCheckedStatus(currNode);
                }
            });
        }
    }
});