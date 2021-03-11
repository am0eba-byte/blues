let $blues := collection('../lyrTexts/?select=*.xml')
let $artists := $blues//artist
return $blues=> count()