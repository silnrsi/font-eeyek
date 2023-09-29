#!/usr/bin/python3
# this is a smith configuration file

# override the default folders
DOCDIR = 'web'

# set the font name and description
APPNAME = 'Eeyek'
FAMILY = APPNAME
DESC_SHORT = 'Font for Meetei Mayek script'

# Get version and authorship information from Regular UFO (canonical metadata)
getufoinfo('source/' + FAMILY + '-Regular' + '.ufo')
# BUILDLABEL = 'beta1'

# Set up the FTML tests
ftmlTest('tools/ftml-smith.xsl')

source = 'source/'

# set up the build parameters from the designspace file(s)
for dspace in ('',):
    designspace(source + FAMILY + dspace + '.designspace',
        target = process('${DS:FILENAME_BASE}.ttf',
            cmd('psfchangettfglyphnames ${SRC} ${DEP} ${TGT}', [source + '${DS:FILENAME_BASE}.ufo']),
        ),
        version = VERSION,
        woff = woff('web/${DS:FILENAME_BASE}',
            metadata = '../source/${DS:FAMILYNAME_NOSPC}-WOFF-metadata.xml'),
        # typetuner='source/typetuner/feat_all.xml',
        script = ['DFLT'],
        pdf = fret(params='-oi')
        )
