describe('NaeLOG Homepage', () => {
	it('should load successfully', () => {
		cy.visit('/');
		cy.contains('ホーム'); // テキスト「ホーム」が表示されていることを確認
	});
});
