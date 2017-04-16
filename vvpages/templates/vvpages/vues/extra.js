{% if perms.vvpages.change_page %}
function isUrl(word) {
    if ( word.substring(0, 1) != "/" ) {
    	return false
    }
    return true
}
{% endif %}