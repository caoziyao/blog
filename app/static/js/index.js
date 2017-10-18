



const __main = function () {
    bindEvents('.page-number', 'click',function() {
          let page = this.dataset.value
            let url = '/page'
            let data = {
              page_no: page
            }
            ajax.post(url,  data, function (response) {
                let r = JSON.parse(response)
                let notes = r.notes;
                let html = template('id-tmp-notelist', {data: notes})
                _e('.wrapper-note-list').innerHTML = html
            })
    })

    bindEvents('.wrapper-catalog-a', 'click', function () {
        let catalogId = this.dataset.catalogid;
        let url = '/catalog'
        let data = {
          catalog_id: catalogId
        }
        ajax.post(url,  data, function (response) {
            let r = JSON.parse(response)
            let notes = r.notes;
            let html = template('id-tmp-notelist', {data: notes})
            _e('.wrapper-note-list').innerHTML = html
        })
    })


    bindEvents('.note-click', 'click', function (event) {
        let target = event.target
        let parent = target.closest('.wiki-note')
        let noteId = parent.dataset.noteid
        log('aaa', noteId, target, parent)
        let url = '/hotspot/incr_click_number'
        let data = {
          note_id: noteId
        }
        ajax.post(url,  data, function (response) {
            let r = JSON.parse(response)
            log('r', r)
            parent.querySelector('.note-click-number').innerHTML = r.number
        })

    })


}


__main()