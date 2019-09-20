'Sample data to test the pubsub internals'

from pubsub import *
from pprint import pprint

post_message('guido', 'i love #python type hinting')
post_message('raymondh', '#python tip: use named tuples')
post_message('barry', 'join a band today')
post_message('raymondh', '#python tip: develop interactively')
post_message('barry', 'learn emacs')
post_message('davin', 'teaching #python today')
post_message('raymondh', '#python tip: have fun programming')
post_message('davin', '#camping tip: always take water')
post_message('barry', 'enums rocks')
post_message('raymondh', '#python tip: never mutate while iterating')
post_message('davin', 'coriander and cilantro come from the same plant')

follow('davin', followed_user='raymondh')
follow('davin', followed_user='barry')



if __name__ == '__main__':
    pprint(search('#python'))
