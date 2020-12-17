#!/bin/bash

vaaka=0
pysty=0

shopt -s nullglob # The script spits errors if this is not set and there are, say, no *.png files.
for image in *.jpg *.JPG *.jpeg *.JPEG *.bmp *.BMP *.png *.PNG;
do
#
##debug numertoita
#width="1"
#high="22323329" 
DIRLAND="./landscape"
DIRVERT="./vertical"
mkdir --parents "$DIRLAND"
mkdir --parents "$DIRVERT"

width=$(identify -format %w\\n "$image")
high=$(identify -format %h\\n "$image")
echo "-------------------------------"

echo "leveys: "$width" ja korkeus: "$high""
echo "$image"
suhde=$(bc -l <<< "scale=0;"$width"/"$high"")
echo $suhde
if (("$suhde" >= "1"))
then
echo "vaaka"
vaaka=$(($vaaka+1))
mv "$image" $DIRLAND;
fi
if (("$suhde" <= "0"))
then
echo "pysty"
pysty=$(($pysty+1))
mv "$image" $DIRVERT;
fi
done

echo "vaaka:"$vaaka""
echo "pysty:"$pysty""
echo "kaikkiaan $(($vaaka+$pysty))"
