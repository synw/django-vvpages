showApps: {
	get: function () {
		if (this.isActive("content")) {
			return "none"
		}
		return "block"
	},
	set: function () {
		if (this.isActive("content")) {
			return "none"
		}
		return "block"
	}
},