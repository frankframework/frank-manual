describe('Tests of frank-manual config - only IAF_Util', () => {
  // Can be enabled if core fixes the warnings omitted here
  xit('Test that the only alert in the status page is about config IAF-Util', () => {
    cy.visit('')
	  cy.get('.alert-warning').should('have.length', 1).within(() => {
      cy.contains('Configuration [IAF_Util]').should('have.length', 1)
    })
  })

  it('Test that only alerts are IAF-Util and FrankConfig-compatibility.xsd', () => {
    cy.visit('')
    cy.get('.alert-warning').omitElementsWithText('FrankConfig-compatibility')
      .should('have.length', 1).each((contents) => {
        cy.wrap(contents).should('contain', 'Configuration [IAF_Util]')
      })
  })
})
