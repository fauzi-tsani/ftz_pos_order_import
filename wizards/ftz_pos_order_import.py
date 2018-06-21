#!/usr/bin/env python
import xlrd
import base64
from io import StringIO,BytesIO
from openerp import models, fields, api
import logging
from openerp.exceptions	import	ValidationError
from openerp.tools.translate import _

_logger = logging.getLogger(__name__)

class ftz_pos_order_import(models.Model):
	_name = 'ftz_pos_order_import.ftz_pos_order_import'
	# _description = 'Description'

	name = fields.Char(
		string='name',size=64,
	)
	upload_file = fields.Binary(
		string='Upload File',
	)

	@api.one
	def do_process(self):
		_logger.info("Import Started %s:%s" % ("1", "2"))
		curr_obj = self
		if not curr_obj.upload_file:
			raise UserError(_('Please Choose The File!'))
		file_name = curr_obj.name
		print "curr_obj.name here",curr_obj.name
		print "file namr here",file_name
		fname = str(file_name.split('.')[1])
		print fname
		# if fname not in ['xls','xlsx']:
		# 	raise UserError(_('Please Choose The File With .xls or .xlsx extension and proper format!'))
		# try:
		# file=base64.decodestring(curr_obj.upload_file)
		# # fp = StringIO()
		# fp = BytesIO()
		# fp.write(file)     
		# wb = xlrd.open_workbook(file_contents=fp.getvalue())
		# wb.sheet_names()
		# sheet_name=wb.sheet_names()
		# sh = wb.sheet_by_index(0)
		# print sh
		# sh = wb.sheet_by_name(sheet_name[0])
		# print sh
		# n_rows = sh.nrows

		file_data = self.upload_file.decode('base64')
		wb = xlrd.open_workbook(file_contents=file_data)
		sheet_names=wb.sheet_names()
		

		for sheet_name in sheet_names:
			sh = wb.sheet_by_name(sheet_name)
			num_cols = sh.ncols
			counter = 0
			for row in range(0, sh.nrows): 
				if counter == 0 : continue
				print ('-'*40)
				print ('Row: %s' % row)   # Print row number
				for col in range(0, num_cols):  # Iterate through columns
					cell_obj = sh.cell(row, col)  # Get cell object by row, col
					print ('Column: [%s] cell_obj: [%s]' % (col, cell_obj))
				counter += 1
				if counter > 10 : break
		error
		
	@api.one
	@api.constrains('name')
	def _check_filename(self):
		if self.upload_file:
			if not self.name: raise ValidationError(_("There is no file"))
		else:
			# Check the file's extension
			tmp = self.name.split('.')
			ext = tmp[len(tmp)-1]
			print ext
			print ext != 'xls'
			print ext != 'xlsx'
			print type(ext)
			print ext in ['xls','xlsx']
			if not ext in ['xls','xlsx']: raise ValidationError(_("The file must be a excel file"))