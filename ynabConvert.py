from optparse import OptionParser
import csv
import sys

def repr_data(hdr, data):
  return ', '.join('%s: %s' % (col, val) for col, val in zip(hdr,data))

BANK_HDR = ['Date',
            'Transaction Type',
            'Check Number',
            'Description',
            'Amount']

class BankTransaction(object):
  """Transaction as read from the BB&T CSV file"""

  def __init__(self, row):
    self.date = row[0]
    self.txType = row[1]
    self.chkNm = row[2]
    self.desc = row[3]

    amtTxt = row[4]
    if amtTxt.startswith('('):
      self.amt = '-%s' % amtTxt[2:-1]
    else:
      self.amt = amtTxt[1:]

    self.data = [self.date,
                 self.txType,
                 self.chkNm,
                 self.desc,
                 self.amt]

  def __repr__(self):
    return repr_data(BANK_HDR, self.data)

YNAB_HDR = ['Date',
            'Payee',
            'Category',
            'Memo',
            'Outflow',
            'Inflow']

class YnabTransaction(object):
  """Transaction to be read into YNAB"""

  def __init__(self, bank_tx):
    self.date = bank_tx.date
    self.payee = bank_tx.desc
    self.category = None
    self.memo = None

    self.inflow = None
    self.outflow = None
    if bank_tx.amt.startswith('-'):
      self.outflow = bank_tx.amt[1:]
    else:
      self.inflow = bank_tx.amt

    self.data = [self.date,
                 self.payee,
                 self.category,
                 self.memo,
                 self.outflow,
                 self.inflow]

  def __repr__(self):
    return repr_data(YNAB_HDR, self.data)


if __name__ == '__main__':
  hdr_written = False

  # Defaults
  inputFile = 'EXPORT.CSV'
  outputFile = 'ynabImport.csv'

  parser = OptionParser(usage="usage: %prog [inputFile] [[outputFile]] ")
  (args, unparsed_args) = parser.parse_args(sys.argv[1:])

  # Read input file as first command line arg, if one is present, if 2 args given, it is input and output file
  if len(unparsed_args) > 0:
    inputFile = unparsed_args[0]

  if len(sys.argv[1:]) > 1:
    outputFile = unparsed_args[1]

  reader = csv.reader(open(inputFile, 'r'))
  writer = csv.writer(open(outputFile, 'w'))

  for row in reader:
    if not hdr_written:
      writer.writerow(YNAB_HDR)
      hdr_written = True
      continue

    bank_tx = BankTransaction(row)
    #print 'bank: (%s)' % bank_tx

    ynab_tx = YnabTransaction(bank_tx)
    #print 'ynab: (%s)' % ynab_tx

    writer.writerow(ynab_tx.data)