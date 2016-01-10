#!/usr/bin/env python

import sys
import imaplib
import getpass
import email
import datetime

EMAIL_ACCOUNT = "shayleewheatley@gmail.com"

M = imaplib.IMAP4_SSL('imap.gmail.com')

try:
    M.login('shayleewheatley@gmail.com', getpass.getpass())
except imaplib.IMAP4.error:
    print "LOGIN FAILED!!! "


rv, mailboxes = M.list()
if rv == 'OK':
    print "Mailboxes:"
    print mailboxes



