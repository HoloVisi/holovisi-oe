#!/bin/sh

git archive --format=tar --prefix=HoloVisi-source-$1/ tags/$1 | bzip2 > HoloVisi-source-$1.tar.bz2
