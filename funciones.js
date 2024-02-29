function consumirApi() {
    // Obtener la URL de la API
    var endpoint = document.getElementById("api").value;

    // Realizar la solicitud fetch
    fetch(endpoint)
        .then(response => {
            return response.json();
        })
        .then(function(data) {
            // Extraer datos relevantes
            var common = [];
            var population = [];
            var region = [];

            for (var i = 0; i < data.length; i++) {
                common.push(data[i].name.common);
                population.push(data[i].population);
                region.push(data[i].region);
            }

            // Asignar colores a las regiones
            var colors = {
                'Asia': '#1f77b4',
                'Europe': '#ff7f0e',
                'Africa': '#2ca02c',
                'Americas': '#d62728',
                'Oceania': '#9467bd'
            };

            // Crear datos para la gráfica
            var data = [];
            for (var i = 0; i < common.length; i++) {
                data.push({
                    x: [common[i]],
                    y: [population[i]],
                    type: 'bar',
                    marker: {
                        color: colors[region[i]]
                    }
                });
            }

            // Generar la gráfica
            Plotly.newPlot('myDiv', data);
        })
        .catch(error => {
            console.log(error);
        });
}