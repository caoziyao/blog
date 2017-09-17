
_e('.dropdwon-box-link').addEventListener('click', function (event) {
    const callback = function (response) {
        let r = JSON.parse(response);
        log('r', r);
        if (r.status === 1){
            let data = r.data;
            let html = template('id-tmp-page-content', { data: data });
            _e('.page-content').innerHTML = html

        }
    };

    let target = event.target;
    let ul = target.closest('.dropdwon-box-ul');
    let url = '/api/load_catalog';
    let catalogId = ul.dataset.catalogid;

    let data = {
        catalog_id: catalogId,
    };

    Api.post(url, JSON.stringify(data), callback)
});

var bindDropDownEvent = function (element) {
    let ele = element;
    _e(ele).addEventListener('click', function (event) {
        let target = event.target;
        let div = target.closest('.wiki-dropdwon-div');
        log('div', div);
        div.querySelector('.dropdwon-box').classList.toggle('hidden')

    })
};

var __main = function () {
     bindDropDownEvent('#id-catalog-btn')
    bindDropDownEvent('#id-new-btn')

}

window.onload = function () {
    __main()
}


