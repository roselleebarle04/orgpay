appModule.controller('MembersController', ['$scope','$http','$routeParams','Member', function($scope, $http, $routeParams, Member) {
	var members = Member.query(function(){
		$scope.members = members.response;
	});

	var member_info = Member.get({id:$routeParams.id}, function(){
		$scope.member_info = member_info;
		console.log(member_info);
	});

	// $http.get('/api/members').then(function(response) {
	// 	console.log(response.data['response']);
	// 	$scope.members = []
	// 	for (r in response.data['response']){
	// 		member = response.data['response'][r];
	// 		console.log(member);
	// 		$scope.members.push(member);
	// 	}
	// 	console.log($scope.members);
        // for (var i = response.data.results.length - 1; i >= 0; i--) {
        //     productsData.push(response.data.results[i]);
        // };
        // if (pageNumber < response.data.pages) {
        //     pageNumber++;
        //     _getPageProducts(pageNumber);
        // } else {
        //     deferred.resolve(productsData)  ;  
        // }
    // });

	console.log('This is Members Page.');
}]);