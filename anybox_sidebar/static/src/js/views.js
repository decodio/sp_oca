openerp.anybox_sidebar = function(instance) {
    
    instance.web.Sidebar.include({
        
        init: function(parent) {
            var self = this;
            this._super(parent);
            var view = this.getParent();
            this.sections = self.get_sections(this.sections, view.fields_view.arch.attrs);
            this.items = {'print' : [], 'other' : [], 'files': []};
            this.fileupload_id = _.uniqueId('oe_fileupload');
            $(window).on(this.fileupload_id, function() {
                var args = [].slice.call(arguments).slice(1);
                self.do_attachement_update(self.dataset, self.model_id,args);
                instance.web.unblockUI();
            });
        },
        
        // remove sections tagged as 'False' in the form definition
        get_sections: function(sections, attrs) {
            var sections2return = JSON.parse(JSON.stringify(sections));
            for(i = 0; i < sections.length; i++){
                if(sections[i].name in attrs){
                    var name = sections[i].name
                    if (attrs[name].toLowerCase() == 'false') {
                        for(j=0; j < sections2return.length; j++){
                            if(sections2return[j].name == sections[i].name){
                                sections2return.splice(j, 1);
                                break;
                            }
                        }
                    }
                }
            }
            return sections2return;
        },
    });
};
