<template lang="html">
	<div class="">
		<div
			:class="{folder: isFolder}"
			@click="toggle"
			@dblclick="changeType">
			{{ model.name }}
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
		toggle: function () {
      if (this.isFolder) {
        this.open = !this.open
      }
    },
		changeType: function () {
      if (!this.isFolder) {
        Vue.set(this.model, 'children', [])
        this.addChild()
        this.open = true
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
      return this.model.children &&
        this.model.children.length
    }
  },
	created(){
      this.log('hellcrewate')
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
