<template lang="html">
	<div class="">
		<div
			:class="{folder: isFolder}"
			@click="toggle">
			<div class="" v-on:click="loadNode(model)" >
				{{ model.name }}
			</div>
			<span v-if="isFolder">[{{ open ? '-' : '+' }}]</span>
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

<script>
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
		loadNode: function (model) {
			let that = this
			if (!this.isFolder) {
				let path = model.path
				let url = '/api/tree/load_note'
				let data = {
					path: path,
				}
				this.axios.post(url, JSON.stringify(data)).then( (res) => {
  		    console.log('res', res);
					let data = res.data;
					let content = data.content;
					bus.$emit('showTreeContent', content)
  		  })
  		  .catch( (error) => {
  		    console.log(error);
  		  });
			}

		},
		toggle: function () {
      if (this.isFolder) {
        this.open = !this.open
      }
    },
    addChild: function () {
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
