1. syncdb
2. runserver
3. navigate to http://127.0.0.1:8000/excel/start/
4. One at a time, browse to get the data file from the sample_data folder
   matching the number of the form item. Click submit. Click back to Start Page.
5. Repeat for first five items (all but final relationship import).
6. Check the exports against the import files in sample data by clicking the
   appropriate export button. NOTE The schools one will NOT match except in
   count.
7. Do import item #6. Recheck the exported relationship data.


The trick is the export_dict and import_dict added to the models file in
sbase. This specifies everything. The excel parts don't really have to
do anything.

I'll probably rearrange the views a little to meet my use cases a little
better.


But all in all, it's:
- Flexible
- Pretty easy to set up
- Allows for using multiple columns as keys where you don't have IDs.
- Much faster than batchimport
- WAY WAY simpler than batchimport
