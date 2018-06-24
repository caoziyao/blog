<template lang="html">
	<div class="container">
		<qui-header class="qui-header"></qui-header>

		<div class="main">
			<div v-for="(book, bookIndex) in books" class="book-cell">
				<div class="breadcrump">
					{{ book.name }}
				</div>
				<!-- v-bind:class="{ active: article.isActive}"  -->
				<ul class="list-group">
					<li class="list-group-item"
					v-for="(article, index) in book.article"
					v-on:mouseover="dataDetails"
					v-on:mouseout="hiddenDetail">
						<a a v-bind:href="getGoodsHref(article.path)" target="_Blank">{{ article.name }}</a>
					</li>
				</ul>
			</div>
		</div>
	</div>
</template>

<script>
import quiHeader from '../components/header.vue'
export default {
	components: {
		'qui-header': quiHeader,
	},
	data() {
		return {
			activeIndex: null,
			books: [],
		}
	},
	methods: {
		getGoodsHref(path) {
			return path
		},
		dataDetails(event) {
			let target = event.target
			let parent = target.closest('li.list-group-item')
			parent.classList.add('active')

			// this.activeIndex = index;
		},
		hiddenDetail(event) {
			let target = event.target
			let parent = target.closest('li.list-group-item')
			parent.classList.remove('active')
		}
	},
	created() {
		let url = '/api/book/get_book_list'
		this.axios.get(url).then((res) => {
			console.log('res', res)
			let data = res.data
			if (data) {
			 // this.$store.commit('saveTreeData', data)
				this.books = data
			}
		}).catch((res) => {
			console.log('res', res)
		})
	}
}
</script>

<style lang="css" scroped>
	.main {
		width: 800px;
		margin: 0 auto;
	}
	.book-cell {
		margin-top: 20px;
	}
	.breadcrump {
		background-color: #fff;
		/*padding: 1rem 8px;*/
		padding-left: 8px;
		margin-bottom: 0;
		/*font-weight: bold;*/
	}

	.list-group {
		display: flex;
		flex-direction: column;
		padding-left: 0;
		margin-bottom: 0;
		margin-top: 5px;
	}

	.list-group-item {
		/*display: flex;
    justify-content: space-between;*/
    /*font-size: 14px;*/
    /*font-weight: bold;*/
		position: relative;
    display: block;
    padding: .75rem 1.25rem;
    margin-bottom: -1px;
    background-color: #fff;
    border: 1px solid rgba(0,0,0,.125);
		cursor: pointer;
	}

	.active {
		background: #ddd;
	}
</style>
