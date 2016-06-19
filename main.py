import threading
#from queue import Queue   #this is for python 3.x
import Queue   #this is for python 2.x
from spider import Spider
from domain import *
from general import *

PROJECT_NAME = 'thenewboston'
HOMEPAGE = 'https://thenewboston.com/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue.Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)