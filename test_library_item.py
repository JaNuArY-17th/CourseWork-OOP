import pytest
from library_item import LibraryItem

def test_library_item_init():
    item = LibraryItem("Test Movie", "Test Director", 4, 100, "test_image.jpg")
    assert item.name == "Test Movie"
    assert item.director == "Test Director"
    assert item.rating == 4
    assert item.play_count == 100
    assert item.image_path == "test_image.jpg"

def test_library_item_name_setter():
    item = LibraryItem("Test Movie", "Test Director", 4, 100, "test_image.jpg")
    with pytest.raises(ValueError):
        item.name = ""

def test_library_item_director_setter():
    item = LibraryItem("Test Movie", "Test Director", 4, 100, "test_image.jpg")
    with pytest.raises(ValueError):
        item.director = ""

def test_library_item_rating_setter():
    item = LibraryItem("Test Movie", "Test Director", 4, 100, "test_image.jpg")
    with pytest.raises(ValueError):
        item.rating = 6
    with pytest.raises(ValueError):
        item.rating = -1

def test_library_item_play_count_setter():
    item = LibraryItem("Test Movie", "Test Director", 4, 100, "test_image.jpg")
    with pytest.raises(ValueError):
        item.play_count = -1

def test_library_item_image_path_setter():
    item = LibraryItem("Test Movie", "Test Director", 4, 100, "test_image.jpg")
    with pytest.raises(ValueError):
        item.image_path = ""

def test_library_item_info():
    item = LibraryItem("Test Movie", "Test Director", 4, 100, "test_image.jpg")
    assert item.info() == "Test Movie - Test Director - ****"

def test_library_item_stars():
    item = LibraryItem("Test Movie", "Test Director", 4, 100, "test_image.jpg")
    assert item.stars() == "****"

def test_library_item_str():
    item = LibraryItem("Test Movie", "Test Director", 4, 100, "test_image.jpg")
    assert str(item) == "Test Movie,Test Director,4,100,test_image.jpg"