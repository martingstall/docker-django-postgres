console.log("👋 Hello world!")

const template = document.createElement('template');
template.innerHTML = `
<style>
    :host {
        display: block;
        font-family: sans-serif;
        color: darkcyan;
    }
</style>
<div class="item">
    <p></p>
</div>
`;

class SampleItem extends HTMLElement {
    constructor() {
        super();
        this._shadowRoot = this.attachShadow({ 'mode': 'open' });
        this._shadowRoot.appendChild(template.content.cloneNode(true));

        this._text = '';

        this.$item = this._shadowRoot.querySelector('.item');
        this.$text = this._shadowRoot.querySelector('p');
    }

    connectedCallback() {
        if (!this.hasAttribute('text')) {
            this.setAttribute('text', 'Sample Item With No Text Provided');
        }

        this._renderTodoItem();
    }

    _renderTodoItem() {
        this.$text.innerHTML = this._text;
    }

    static get observedAttributes() {
        return ['text'];
    }

    attributeChangedCallback(name, oldValue, newValue) {
        this._text = newValue;
    }
}

window.customElements.define('sample-item', SampleItem);
