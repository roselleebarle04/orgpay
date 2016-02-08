appModule.controller('MembersController', ['$scope','$http','$routeParams','Member', function($scope, $http, $routeParams, Member) {
	var members = Member.query(function(){
		$scope.members = members.response;
		console.log(members.response);
	});

	var member_info = Member.get({id:$routeParams.id}, function(){
		$scope.member_info = member_info;
		console.log(member_info);
	});

	$scope.addMemberForm = {};
	$scope.processForm = function(){
		$http({
			method: 'POST',
			url: '/api/members/',
			data: $.param($scope.addMemberForm),
			headers: { 'Content-Type': 'application/json' }
		})
		.success(function(data){
			console.log(data);
			if (!data.success) {
				// if not successful, bind errors to error variables
				$scope.errorName = data.errors.name;
				$scope.errorSuperhero = data.errors.superheroAlias;
			} else {
				// if successful, bind success message to message
				$scope.message = data.message;
			}
		})
	};
}]);