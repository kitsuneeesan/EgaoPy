var load = document.getElementById("load");

const kambing = () => {
  if (document.getElementById("macan").files.length == 0) {
    alert("no files selected");
  } else {
    load.className = "imgload";
    load.src = "static/svg/load.svg";
    submitClick();
  }
};

const submitClick = () => {
  const formData = new FormData();
  const fileField = document.querySelector('input[type="file"]');
  const today = new Date()

  formData.append("photo", fileField.files[0]);
  formData.append("date", today.toLocaleString());

  fetch('/uploader', { method: "POST", body: formData, })
    .then((response) => {
      return response.json();
    }).then((res) => {
      if (res.success == true) {
        load.className = "imgloadmute";
        const image = document.getElementById("imgplace");
        image.className = "imgview"
        image.src = `data:image/png;base64,${res.image}`;
      }
    });
};
