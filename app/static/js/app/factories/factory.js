appModule.factory('Member', ['$resource', function($resource){
	return $resource('/api/members/:id', {}, {
		query: { method: 'GET', isArray: false }
	});
}])