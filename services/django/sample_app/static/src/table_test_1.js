import {LitElement, css, html} from '../web_modules/lit-element.js';

class LitTable extends LitElement {
    static get properties() {
        return {
            data: { type: Array },
            url: { type: String },
        };
    }

    constructor() {
        super();
        this.data = [];
        this.dataIndexes = [];
    }

    static get styles() {
        return css`
            body {
                background-color: red;
            }
            
            .table tr.even {
                background-color: #f1f1f1;
            }
            .table tr.odd {
                background-color: #fff;
            }
        `;
    }

    render() {
        let buildHtml = '<table class="table">';

        buildHtml += '<tr>';
        for (var i = 1; i <= 1; i++) {
            for (var key in this.data[i]) {
                this.dataIndexes.push(key)
                buildHtml += '<td>' + key + '</td>';
            }
        }
        buildHtml += '</tr>';

        for (var d = 0; d < this.data.length; d++) {
            buildHtml += '<tr>';
            for (var x = 0; x < this.dataIndexes.length; x++) {
                buildHtml += '<td>' + this.data[d][this.dataIndexes[x]] + '</td>';
            }
            buildHtml += '</tr>';
        }
        buildHtml += '</table>';

        this.shadowRoot.innerHTML = buildHtml;
        //return html`<table>${this.buildHtmlRows}</table>`;
    }

    firstUpdated() {
        (async () => {
            //let response = await fetch('https://rickandmortyapi.com/api/character/');
            let response = await fetch(this.url);
            let data = await response.json();
            this.data = data;
        })();
    }
}

window.customElements.define('lit-table', LitTable);
