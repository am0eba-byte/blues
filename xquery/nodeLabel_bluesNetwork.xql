xquery version "3.1";
declare variable $ThisFileContent :=
string-join(
let $blues := collection('/db/blues')
let $artists := $blues//artist ! normalize-space() => distinct-values() => sort()
for $a in $artists
let $titles := $blues[.//artist ! normalize-space() = $a]//title ! normalize-space() => distinct-values()
        for $t in $titles
        let $songwriters := $blues[.//title ! normalize-space() = $t]//songwriter ! normalize-space() => distinct-values()
        for $s in $songwriters
            let $tokens := substring-after($s, 'by ') ! tokenize(., ' / ') ! normalize-space() => distinct-values()
            for $k in $tokens

        
return concat ($a, "&#x9;", "PerformArtist", "&#x9;", $t, "&#x9;", "Song", "&#x9;", $k, "&#x9;", "Songwriter"), "&#10;") ;


let $filename := "nodeLabel_BluesNetwork-ebb.tsv"
let $doc-db-uri := xmldb:store("/db/mqb5995", $filename, $ThisFileContent, "text/plain")
return $doc-db-uri
(: (: output: http://newtfire.org:8338/exist/rest/db/mqb5995/nodeLabel_BluesNetwork-ebb.tsv :) :)

    (:for $a in $artists
    return $a:)
    (:let $songwriters := $blues[.//artist ! normalize-space() = $a]//songwriter
        for $s in $songwriters:)
    (:let $titles := $blues[.//artist ! normalize-space() = $a]//title ! normalize-space() => distinct-values()
        for $t in $titles:)
       (: return $s:)
        (:let $songwriters := $blues[.//title ! normalize-space() = $t]//songwriter
            for $s in $songwriters:)