var appModule = angular.module('appModule',['ngRoute', 'ngResource']);

appModule.config(['$routeProvider', function($routeProvider) {
	$routeProvider.
		when('/', {
			templateUrl: 'static/partials/home.html'
		}).
		when('/collections/add', {
			templateUrl: 'static/partials/add_collection.html'
		}).
		when('/collections/:id', {
			templateUrl: 'static/partials/collection_info.html'
		}).
		when('/collections', {
			templateUrl: 'static/partials/collections.html'
		}).
		when('/members/add', {
			templateUrl: 'static/partials/add_member.html'
		}).
		when('/members/:id', {
			templateUrl: 'static/partials/member_info.html'
		}).
		when('/members', {
			templateUrl: 'static/partials/members.html'
		}).
		otherwise({
			redirectTo: '/'
		});
}]);

appModule.controller("MainController", ['$scope','$http','$rootScope', function($scope,$http,$rootScope) {
	console.log("This is Organization Management Portal site.");
}]);