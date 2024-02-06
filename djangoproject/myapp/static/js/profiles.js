let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
  columnDefs: [
    { className: "centered", targets: [0, 1, 2, 3, 4, 5, 6, 7] },
    { orderable: false, targets: [6, 7] },
    { searchable: false, targets: [0, 6, 7] },
  ],
  destroy: true,
};

const initDataTable = async () => {
  if (dataTableIsInitialized) {
    dataTable.destroy();
  }
  await listProfile();
  dataTable = $("#datatable-profiles").DataTable({});

  dataTableIsInitialized = true;
};

const listProfile = async () => {
  try {
    const response = await fetch("../list_profile");
    const data = await response.json();
    let content = "";
    data.profiles.forEach((profiles, index) => {
      content += `<tr>
        <td>${index + 1}</td>
        <td>${profiles.user_id}</td>
        <td>${profiles.rol}</td>
        <td>${profiles.nombres_apellidos}</td>
        <td>${profiles.cedula}</td>
        <td>${profiles.direccion}</td>
        <td>${profiles.telefono}</td>
        <td>${profiles.referencia}</td>
        <td>
            <a href="../editarprofile"><button class='btn btn-sm btn-primary'><i class='fa-solid fa-pencil'></i></button></a>
        </td>
      </tr>`;
    });
    tableBody_profiles.innerHTML = content;
  } catch (ex) {
    alert(ex);
    console.error(
      "La propiedad 'nombre' no existe en la respuesta del servidor."
    );
  }
};
window.addEventListener("load", async () => {
  await initDataTable();
});
