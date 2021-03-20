xquery version "3.1";
declare variable $ThisFileContent:=

<html>
    <head><title>Blues Stuff</title></head>
    <body>
        <h1>Artists and Song Titles</h1>
<table>
    <tr><th>Artist name</th><th>Song Titles List</th></tr>

{
let $blues := collection('/db/blues')
let $metadata := $blues//metadata
let $bessie := $blues//artist[. ! normalize-space() = "Bessie Smith"]
let $artists := $blues//artist ! normalize-space() => distinct-values() => sort()
for $a in $artists
let $songs := $blues[.//artist ! normalize-space() = $a]//title
return 
   
   <tr>
       <td>{$a}</td>
       <td><ol>{for $s in $songs 
       return
           <li>{$s/text()}</li>
       }
           </ol>
       </td>
     </tr>
}
</table>
</body>
</html> ;

let $filename := "bluesArtistTable.html"
let $doc-db-uri := xmldb:store("/db/2021-ClassExamples", $filename, $ThisFileContent, "html")
return $doc-db-uri 
(: output at :http://newtfire.org:8338/exist/rest/db/2021-ClassExamples/bluesArtistTable.html ) :)        


