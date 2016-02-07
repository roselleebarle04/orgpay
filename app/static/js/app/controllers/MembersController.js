appModule.controller('MembersController', ['$scope','$http', 'Member', function($scope, $http, Member) {
	$scope.members = Member.query();
	console.log($scope.members);

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