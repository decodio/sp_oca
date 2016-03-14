openerp.list_multiheader_visual_export = function (instance) {

    instance.web.ListViewMultiHeader.include({
        get_export_fields_and_headers: function(){
            var fields = [];
            var headers = [];
            var rowspan = this.multiheader_columns.length
            _(this.multiheader_columns).each(function(row){
                header = [];
                _(row).each(function(column) {
                    if (column.tag === 'field' && column.invisible != '1'){
                        header.push({
                            string: column.string,
                            rowspan: rowspan,
                            colspan: 1});
                    }else{
                        if (column.tag === 'group') {
                            header.push({
                                string: column.string,
                                rowspan: 1,
                                colspan: column.colspan});
                        }
                    }
                });
                headers.push(header);
                rowspan -= 1;
            });
            if(!this.visible_columns[0].name){
                headers[0].splice(0, 0, {
                    string: this.visible_columns[0].string,
                    colspan: 1,
                    rowspan: this.multiheader_columns.length
                });
            }
            _(this.visible_columns).each(function(c){
                if (c.name) fields.push(c.name);
            });
            return [fields, headers];
        },
    });
};
