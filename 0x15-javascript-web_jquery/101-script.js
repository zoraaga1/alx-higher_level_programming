<!DOCTYPE html>
<html lang="en">
<head>
    <title>List Manipulation</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
        $(document).ready(function(){
            // Add item to the list
            $("#add_item").click(function(){
                $("ul.my_list").append("<li>Item</li>");
            });

            // Remove last item from the list
            $("#remove_item").click(function(){
                $("ul.my_list li:last-child").remove();
            });

            // Clear all items from the list
            $("#clear_list").click(function(){
                $("ul.my_list").empty();
            });
        });
    </script>
</head>
<body>
    <div id="add_item">Add Item</div>
    <div id="remove_item">Remove Item</div>
    <div id="clear_list">Clear List</div>
    <ul class="my_list"></ul>
</body>
</html>
