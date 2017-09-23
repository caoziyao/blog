


const __main = function () {

    bindEvents('.page-number', function() {
          let page = this.dataset.value
            let url = '/page'

            let data = {
              page_no: page
            }

            ajax.post(url,  data, function (response) {
                let r = JSON.parse(response)
                let notes = r.notes;

                let html = template('id-tmp-notelist', {data: notes})

                log('html', html)
                _e('.wrapper-note-list').innerHTML = html
            })
    })


    bindEvents('.wrapper-catalog-a', function () {
           let catalogId = this.dataset.catalogid;

           log('catalogId', catalogId, this)
            let url = '/catalog'

            let data = {
              catalog_id: catalogId
            }

            ajax.post(url,  data, function (response) {
                let r = JSON.parse(response)
                let notes = r.notes;

                let html = template('id-tmp-notelist', {data: notes})

                log('html', html)
                _e('.wrapper-note-list').innerHTML = html
            })
    })

}


__main()