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
  await listProducto();
  dataTable = $("#datatable-productos").DataTable({});

  dataTableIsInitialized = true;
};

const listProducto = async () => {
  try {
    const response = await fetch("../list_producto");
    const data = await response.json();
    let content = "";
    data.productos.forEach((productos, index) => {
      content += `<tr>
            <td>${index + 1}</td>
            <td>${productos.nombre}</td>
            <td>${productos.codigo}</td>
            <td>${productos.stock}</td>
            <td>${productos.precio}</td>
            <td>${productos.precioventa}</td>
            <td>${productos.id_categoria}</td>
            <td>
            <a href="../editar_producto/${
              productos.codigo
            }"><button class='btn btn-sm btn-primary'><i class='fa-solid fa-pencil'></i></button></a>
            <a href="../eliminar_producto/${
              productos.codigo
            }"><button class='btn btn-sm btn-danger'><i class='fa-solid fa-trash-can'></i></button></a>
            <a href="../mostrar_producto/${
              productos.codigo
            }"><button class='btn btn-sm btn-secondary'><i class='fa-solid fa-binoculars'></i></button></a>
        </td>
        </tr>`;
    });
    tableBody_productos.innerHTML = content;
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
