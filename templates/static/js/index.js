(() => {
  "use strict";

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  const forms = document.querySelectorAll(".needs-validation");

  // Loop over them and prevent submission
  Array.from(forms).forEach((form) => {
    form.addEventListener(
      "submit",
      (event) => {
        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();
        }

        form.classList.add("was-validated");
      },
      false
    );
  });
})();

// Toast
document.addEventListener("DOMContentLoaded", (event) => {
  var myToastEl = document.getElementById("myToast");
  var myToast = new bootstrap.Toast(myToastEl, {
    animation: true,
    autohide: true,
    delay: 5000,
  });

  myToast.show();
});

// Ajax Handling
function crudUserSubmitForm(event) {
  event.preventDefault();
  form = document.getElementById("userCrudForm");
  csrf_token = event.target[0].value;
  title = event.srcElement[1].value;
  age = event.srcElement[2].value;
  stat = event.srcElement[3].value;
  let data = {
    title: title,
    age: age,
    stat: stat,
  };
  form.reset();
  $.ajax({
    url: `/core/add_user`,
    type: "POST",
    data: {
      csrfmiddlewaretoken: csrf_token,
      data: JSON.stringify(data),
    },
    success: function (response) {
      var myToastEl = document.getElementById("ajaxToast");
      var toastBody = document.getElementById("ajaxToastBody");
      var myToast = new bootstrap.Toast(myToastEl, {
        animation: true,
        autohide: true,
        delay: 5000,
      });
      toastBody.innerHTML = response.content;
      myToast.show();
      $("#createUserModal").modal("hide");
      let table = document.getElementById("usersListTable");
      let row = table.insertRow(1);
      row.setAttribute("id", `row_${response.id}`);
      let cell1 = row.insertCell(0);
      let cell2 = row.insertCell(1);
      let cell3 = row.insertCell(2);
      let cell4 = row.insertCell(3);
      let cell5 = row.insertCell(4);

      cell1.innerHTML = response.id;
      cell2.innerHTML = response.title;
      cell3.innerHTML = response.age;
      cell4.innerHTML = `<span class="badge text-bg-success">${response.status}</span>`;
      cell5.innerHTML = `
            <button type="submit" class="btn btn-danger" onclick="deleteUser('${response.csrftoken}', ${response.id})">
              Delete
            </button>
        `;
    },
    error: function (status, error) {
      console.error("Error occurred:", status, error);
    },
  });
}

// Delete User
function deleteUser(csrf, id) {
  let deleteRow = document.getElementById(`row_${id}`);
  $.ajax({
    url: "/core/delete_user",
    type: "POST",
    data: {
      csrfmiddlewaretoken: csrf,
      data: JSON.stringify({ id: id }),
    },
    success: function (response) {
      var myToastEl = document.getElementById("ajaxToast");
      var toastBody = document.getElementById("ajaxToastBody");
      var myToast = new bootstrap.Toast(myToastEl, {
        animation: true,
        autohide: true,
        delay: 5000,
      });
      if (response.status == 200) {
        deleteRow.remove();
        toastBody.innerHTML = response.content;
      } else if ((response.status = 404)) {
        toastBody.innerHTML = response.content;
        console.error("Error occurred:", response.status, response.content);
      }
      myToast.show();
    },
    error: function (status, error) {
      console.error("Error occurred:", status, error);
    },
  });
}

/*Theme Toggle */
$(document).ready(() => {
  const body = document.querySelector("body");
  const checkbox = document.getElementById("theme");
  loadTheme();
  checkbox.addEventListener("change", (e) => {
    const currentTheme = e.target.checked;
    updateTheme(currentTheme);
    updateThemeLocalStorage(currentTheme);
  });
  function loadTheme() {
    window.localStorage.getItem("dark")
      ? (checkbox.checked =
          JSON.parse(window.localStorage.dark) == true ? false : true)
      : updateThemeLocalStorage(checkbox.checked);
    updateTheme(!JSON.parse(window.localStorage.dark));
  }
  function updateTheme(currentTheme) {
    body.setAttribute("data-bs-theme", currentTheme ? "light" : "dark");
  }
  function updateThemeLocalStorage(currentTheme) {
    window.localStorage.dark = !currentTheme;
  }
});
