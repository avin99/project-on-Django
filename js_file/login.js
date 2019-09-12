function myFunction(){s
	var x = document.getElementById("change");
	var y = document.getElementById("change1");
	if( x.style.display === "none" && y.style.display === "block"){
		x.style.display = "block";
		y.style.display = "none";
	} else {
		x.style.display = "none";
		y.style.display = "block";
	}
}