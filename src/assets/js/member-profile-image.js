var image_coord_x1;
var image_coord_x2;
var image_coord_y1;
var image_coord_y2;

function enableCropping() {
    $('#member-image').Jcrop({
        onSelect: saveCoords,
        setSelect: [50, 50, 500, 500],
        aspectRatio: 1.0
    });
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
        $('#member-image').attr('src', ev.target.result);
        $('#member-image').attr('title', photo.name);
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
    var image_coords = null
    if (left_x && top_y && right_x && bottom_y) {
        image_coords = [left_x, top_y, right_x, bottom_y].join(',');
    }
    $('#image_coords').val(image_coords);
    $('#member-image-form').submit();
}