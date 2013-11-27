$(document).ready(function() {
    $(".nav-link").click( function(){
        highlightLink(this.href);
    });
});

$(document).ready(function() {
    var url = document.URL;
    highlightLink(url);
});

function highlightLink(link) {
    var accessed_page = link.substring(link.lastIndexOf('/'));
    link_st_ind = link.indexOf('#');
    if(link_st_ind != -1) {
        sec_num = parseInt(link.substring(link_st_ind+8));
        if(sec_num == currentSectionNumber) return;
        $('#section'+currentSectionNumber).slideToggle();
        $(link.substring(link_st_ind)).slideToggle();
        currentSectionNumber = sec_num;
    }
    $(".nav-link").each(function(){
        st_ind = this.href.indexOf('#');
        if((st_ind != -1) && (this.href.substring(st_ind) == link.substring(link_st_ind))) {
            this.style.textDecoration="overline";
        } else if(accessed_page == this.href.substring(this.href.lastIndexOf('/'))) {
            this.style.textDecoration="overline";
        } else {
            this.style.textDecoration="none";
        }
    });
}