<template lang="html">
	<div class="">
		<div
			:class="{folder: isFolder}"
			@click="toggle">
			<div class="" v-on:click="loadNode(model)" >
				<span v-if="isFolder">
						<i v-if="open" class="fa fa-folder-open-o fa-lg"></i>
						<i v-else class="fa fa-folder-o fa-lg"></i>
				</span>
				{{ model.name }}
			</div>

		</div>
		<div v-show="open" v-if="isFolder" class="chliden">
			<item
				class="item"
				v-for="(model, index) in model.children"
				:key="index"
				:model="model">
			</item>
			<li class="add" @click="addChild">+</li>
		</div>
	</div>
</template>

<script scoped>
import bus from '../assets/eventBus'
export default {
	name: 'item',
	props: {
    model: Object
  },
	data() {
		return {
			open: false,
		}
 	},
	methods: {
		loadNode(model) {
			let that = this
			if (!this.isFolder) {
				let path = model.path
				let url = '/api/tree/load_note'
				let data = {
					path: path,
				}
				this.axios.post(url, JSON.stringify(data)).then( (res) => {
					let data = res.data;
					let ret = {
						content: data.content,
						path: data.path,
						filename: data.filename,
					}
					// bus总线，发送 content 给自定义 showTreeContent 事件
					bus.$emit('showTreeContent', ret)
  		  })
  		  .catch( (error) => {
  		    console.log(error);
  		  });
			}

		},
		toggle () {
      if (this.isFolder) {
        this.open = !this.open
				this.model.open = this.open
				// this.$store.state.
      }
    },
    addChild () {
      this.model.children.push({
        name: 'new stuff'
      })
    }
	},
	computed: {
    isFolder: function () {
			return this.model.isFolder
    }
  },
	// 由于数据更改导致的虚拟 DOM 重新渲染和打补丁，在这之后会调用该钩子。
	updated() {
		let model = this.model
		this.open = model.open
	}
}
</script>

<style lang="css">
.item {
  cursor: pointer;
}
.bold {
  font-weight: bold;
}
.chliden {
	position: relative;
	left: 20px;
}
ul {
  padding-left: 1em;
  line-height: 1.5em;
  list-style-type: none;
}

</style>
