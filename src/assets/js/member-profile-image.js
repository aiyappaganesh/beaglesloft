var image_coord_x1;
var image_coord_x2;
var image_coord_y1;
var image_coord_y2;

var jcrop_api;

function enableCropping() {
    $('#member-image').Jcrop({
        onSelect: saveCoords,
        setSelect: [50, 50, 500, 500],
        bgColor: 'transparent',
        aspectRatio: 1.0
    }, function(){ jcrop_api = this; });
}

function displayPhotoThumbnail(e) {
    var photo_files = e.target.files;
    var photo_file = photo_files[0];

    if (!photo_file.type.match('image.*')) {
        alert('Not an image file');
        $('#member-image-upload').focus();
        return;
    }

    var file_reader = new FileReader();
    file_reader.onload = (function(photo) {
      return function(ev) {
        if(jcrop_api) {
            jcrop_api.destroy();
            $('#member-image').css({height:'auto',width:'auto'});
        }
        $('#member-image').attr('src', ev.target.result);
        $('#member-image').attr('title', photo.name);

        if ($('#member-image').width() > 800){
            $('#member-image').width(800);
        }
        orig_height = $('#member-image').height();
        orig_width = $('#member-image').width();
        aspect_ratio = orig_width/orig_height;
        if ($('#member-image').height() > 600){
            $('#member-image').height(600);
            $('#member-image').width(aspect_ratio*600);
        }
        enableCropping();
      };
    })(photo_file);

    file_reader.readAsDataURL(photo_file);
}

function saveCoords(c){
    image_coord_x1 = c.x;
    image_coord_x2 = c.x2;
    image_coord_y1 = c.y;
    image_coord_y2 = c.y2;
};

$(document).ready(function () {
    document.getElementById('member-image-upload').addEventListener('change', displayPhotoThumbnail, false);
})

function saveMemberImage() {
    var width = $('#member-image').width();
    var height = $('#member-image').height();
    var left_x = image_coord_x1/width;
    var top_y = image_coord_y1/height;
    var right_x = image_coord_x2/width;
    var bottom_y = image_coord_y2/height;
    var image_coords = null;
    if (left_x != null && top_y != null && right_x != null && bottom_y != null) {
        image_coords = [left_x, top_y, right_x, bottom_y].join(',');
    }
    $('#image_coords').val(image_coords);
    $('#member-image-form').submit();
}