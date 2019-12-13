#!/usr/bin/python3
# encoding: utf-8
# this is a smith configuration file - http://scripts.sil.org/smith

# set some default output folders (most are already set by default)
DOCDIR = 'web'
STANDARDS = 'tests/reference'

# set the font name and description
APPNAME = 'Eeyek'
FAMILY = APPNAME
DESC_SHORT = 'Font for Meetei Mayek script'

# Get version and authorship information from Regular UFO (canonical metadata)
getufoinfo('source/' + FAMILY + '-Regular' + '.ufo')
# BUILDLABEL = 'alpha1'

# Set up the FTML tests
ftmlTest('tools/ftml-list.xsl')

# set the build and test parameters
TESTSTRING = u'\uABC0'
source = 'source/'

# set up the build parameters from the designspace file(s)
for dspace in ('',):
    designspace(source + FAMILY + dspace + '.designspace',
        target = process('${DS:FILENAME_BASE}.ttf',
            cmd('${PSFCHANGETTFGLYPHNAMES} ${SRC} ${DEP} ${TGT}', [source + '${DS:FILENAME_BASE}.ufo']),
        ),
        version = VERSION,
        woff = woff('web/${DS:FILENAME_BASE}.woff', params='-v ' + VERSION + ' -m ../source/${DS:FAMILYNAME}-WOFF-metadata.xml'),
        # typetuner='source/typetuner/feat_all.xml',
        script = ['DFLT'],
        fret = fret(params='-oi')
        )


# declare other local variables or utilities
def configure(ctx):
    ctx.find_program('psfchangettfglyphnames')
